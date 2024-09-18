<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <author>Marcos Henrique - Dev. Ninja</author>
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>374</width>
    <height>538</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>374</width>
    <height>538</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1000000</width>
    <height>10000</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Client v1.0.1</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.539455, y2:0.301, stop:0 rgba(255, 175, 175, 233), stop:1 rgba(255, 231, 231, 255))</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout_3">
    <item row="2" column="0">
     <widget class="Line" name="line">
      <property name="orientation">
       <enum>Qt::Orientation::Horizontal</enum>
      </property>
     </widget>
    </item>
    <item row="5" column="0">
     <widget class="QFrame" name="options">
      <property name="enabled">
       <bool>false</bool>
      </property>
      <property name="autoFillBackground">
       <bool>false</bool>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgba(239, 239, 239, 160)
</string>
      </property>
      <property name="frameShape">
       <enum>QFrame::Shape::StyledPanel</enum>
      </property>
      <property name="frameShadow">
       <enum>QFrame::Shadow::Raised</enum>
      </property>
      <layout class="QGridLayout" name="gridLayout">
       <item row="1" column="0">
        <widget class="QFrame" name="frame_2">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="layoutDirection">
          <enum>Qt::LayoutDirection::LeftToRight</enum>
         </property>
         <property name="frameShape">
          <enum>QFrame::Shape::StyledPanel</enum>
         </property>
         <property name="frameShadow">
          <enum>QFrame::Shadow::Raised</enum>
         </property>
         <layout class="QHBoxLayout" name="horizontalLayout_2">
          <item>
           <widget class="QRadioButton" name="Movie">
            <property name="text">
             <string>Movie</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QRadioButton" name="Audio">
            <property name="text">
             <string>Audio</string>
            </property>
           </widget>
          </item>
         </layout>
        </widget>
       </item>
       <item row="3" column="0">
        <widget class="QPushButton" name="Download">
         <property name="text">
          <string>Download</string>
         </property>
         <property name="default">
          <bool>false</bool>
         </property>
         <property name="flat">
          <bool>false</bool>
         </property>
        </widget>
       </item>
       <item row="2" column="0">
        <widget class="QComboBox" name="SelectQuality">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(255, 255, 255)</string>
         </property>
         <property name="placeholderText">
          <string>Content Quality</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
    <item row="3" column="0">
     <widget class="QFrame" name="metadata">
      <property name="autoFillBackground">
       <bool>false</bool>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgba(239, 239, 239, 120)
</string>
      </property>
      <property name="frameShape">
       <enum>QFrame::Shape::StyledPanel</enum>
      </property>
      <property name="frameShadow">
       <enum>QFrame::Shadow::Raised</enum>
      </property>
      <layout class="QGridLayout" name="gridLayout_2">
       <item row="4" column="1">
        <widget class="QLabel" name="views">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(255, 255, 255)</string>
         </property>
         <property name="text">
          <string>Views</string>
         </property>
         <property name="alignment">
          <set>Qt::AlignmentFlag::AlignCenter</set>
         </property>
        </widget>
       </item>
       <item row="4" column="0">
        <widget class="QLabel" name="channel">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(255, 255, 255)</string>
         </property>
         <property name="text">
          <string>Channel</string>
         </property>
         <property name="alignment">
          <set>Qt::AlignmentFlag::AlignCenter</set>
         </property>
        </widget>
       </item>
       <item row="0" column="0" colspan="2">
        <widget class="QLabel" name="title">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(255, 255, 255)</string>
         </property>
         <property name="text">
          <string>TITLE</string>
         </property>
         <property name="alignment">
          <set>Qt::AlignmentFlag::AlignCenter</set>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
    <item row="1" column="0">
     <widget class="QFrame" name="thumbnail">
      <property name="autoFillBackground">
       <bool>false</bool>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgba(239, 239, 239, 120)
</string>
      </property>
      <property name="frameShape">
       <enum>QFrame::Shape::StyledPanel</enum>
      </property>
      <property name="frameShadow">
       <enum>QFrame::Shadow::Raised</enum>
      </property>
      <layout class="QVBoxLayout" name="verticalLayout_2">
       <item>
        <widget class="QLabel" name="label">
         <property name="styleSheet">
          <string notr="true"/>
         </property>
         <property name="text">
          <string>Media Thumbnail</string>
         </property>
         <property name="alignment">
          <set>Qt::AlignmentFlag::AlignCenter</set>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_2">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(255, 255, 255)</string>
         </property>
         <property name="text">
          <string/>
         </property>
         <property name="pixmap">
          <pixmap resource="sources/images.qrc">:/images/hand_icon.ico</pixmap>
         </property>
         <property name="scaledContents">
          <bool>true</bool>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
    <item row="0" column="0">
     <widget class="QFrame" name="frame">
      <property name="autoFillBackground">
       <bool>false</bool>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgba(239, 239, 239, 120)
</string>
      </property>
      <property name="frameShape">
       <enum>QFrame::Shape::StyledPanel</enum>
      </property>
      <property name="frameShadow">
       <enum>QFrame::Shadow::Raised</enum>
      </property>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QLabel" name="url">
         <property name="text">
          <string>Video Url</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="urlEntry">
         <property name="styleSheet">
          <string notr="true">background-color: rgba(255, 255, 255, 200)</string>
         </property>
         <property name="placeholderText">
          <string>insert your url or id here</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
    <item row="4" column="0">
     <widget class="Line" name="line_2">
      <property name="orientation">
       <enum>Qt::Orientation::Horizontal</enum>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources>
  <include location="sources/images.qrc"/>
 </resources>
 <connections/>
</ui>
