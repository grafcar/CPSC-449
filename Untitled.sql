CREATE TABLE Users (
    UserID INT AUTO_INCREMENT,
    Username VARCHAR(50),
    Email VARCHAR(50),
    Password VARCHAR(50),
    PRIMARY KEY(UserID)
);

CREATE TABLE Blogs (
    BlogID INT AUTO_INCREMENT,
    UserID INT,
    Title VARCHAR(100),
    Content TEXT,
    DatePosted DATETIME,
    PRIMARY KEY(BlogID),
    FOREIGN KEY(UserID) REFERENCES Users(UserID)
);

CREATE TABLE Comments (
    CommentID INT AUTO_INCREMENT,
    UserID INT,
    BlogID INT,
    Comment TEXT,
    DateCommented DATETIME,
    PRIMARY KEY(CommentID),
    FOREIGN KEY(UserID) REFERENCES Users(UserID),
    FOREIGN KEY(BlogID) REFERENCES Blogs(BlogID)
);
