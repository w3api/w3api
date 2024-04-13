---
title: JComboBox
permalink: /Java/JComboBox/
date: 2021-01-11
key: Java.J.JComboBox
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JComboBox.description }}

## Sintaxis
~~~java
@JavaBean(defaultProperty="UI", description="A combination of a text field and a drop-down list.") public class JComboBox<E> extends JComponent implements ItemSelectable, ListDataListener, ActionListener, Accessible
~~~

## Constructores
* [JComboBox()](/Java/JComboBox/JComboBox/)

## Campos
* [actionCommand](/Java/JComboBox/actionCommand)
* [dataModel](/Java/JComboBox/dataModel)
* [editor](/Java/JComboBox/editor)
* [isEditable](/Java/JComboBox/isEditable)
* [keySelectionManager](/Java/JComboBox/keySelectionManager)
* [lightWeightPopupEnabled](/Java/JComboBox/lightWeightPopupEnabled)
* [maximumRowCount](/Java/JComboBox/maximumRowCount)
* [renderer](/Java/JComboBox/renderer)
* [selectedItemReminder](/Java/JComboBox/selectedItemReminder)

## Métodos
* [actionPerformed()](/Java/JComboBox/actionPerformed)
* [actionPropertyChanged()](/Java/JComboBox/actionPropertyChanged)
* [addActionListener()](/Java/JComboBox/addActionListener)
* [addItem()](/Java/JComboBox/addItem)
* [addItemListener()](/Java/JComboBox/addItemListener)
* [addPopupMenuListener()](/Java/JComboBox/addPopupMenuListener)
* [configureEditor()](/Java/JComboBox/configureEditor)
* [configurePropertiesFromAction()](/Java/JComboBox/configurePropertiesFromAction)
* [contentsChanged()](/Java/JComboBox/contentsChanged)
* [createActionPropertyChangeListener()](/Java/JComboBox/createActionPropertyChangeListener)
* [createDefaultKeySelectionManager()](/Java/JComboBox/createDefaultKeySelectionManager)
* [fireActionEvent()](/Java/JComboBox/fireActionEvent)
* [fireItemStateChanged()](/Java/JComboBox/fireItemStateChanged)
* [firePopupMenuCanceled()](/Java/JComboBox/firePopupMenuCanceled)
* [firePopupMenuWillBecomeInvisible()](/Java/JComboBox/firePopupMenuWillBecomeInvisible)
* [firePopupMenuWillBecomeVisible()](/Java/JComboBox/firePopupMenuWillBecomeVisible)
* [getAccessibleContext()](/Java/JComboBox/getAccessibleContext)
* [getAction()](/Java/JComboBox/getAction)
* [getActionCommand()](/Java/JComboBox/getActionCommand)
* [getActionListeners()](/Java/JComboBox/getActionListeners)
* [getEditor()](/Java/JComboBox/getEditor)
* [getItemAt()](/Java/JComboBox/getItemAt)
* [getItemCount()](/Java/JComboBox/getItemCount)
* [getItemListeners()](/Java/JComboBox/getItemListeners)
* [getKeySelectionManager()](/Java/JComboBox/getKeySelectionManager)
* [getMaximumRowCount()](/Java/JComboBox/getMaximumRowCount)
* [getModel()](/Java/JComboBox/getModel)
* [getPopupMenuListeners()](/Java/JComboBox/getPopupMenuListeners)
* [getPrototypeDisplayValue()](/Java/JComboBox/getPrototypeDisplayValue)
* [getRenderer()](/Java/JComboBox/getRenderer)
* [getSelectedIndex()](/Java/JComboBox/getSelectedIndex)
* [getSelectedItem()](/Java/JComboBox/getSelectedItem)
* [getSelectedObjects()](/Java/JComboBox/getSelectedObjects)
* [getUI()](/Java/JComboBox/getUI)
* [getUIClassID()](/Java/JComboBox/getUIClassID)
* [hidePopup()](/Java/JComboBox/hidePopup)
* [insertItemAt()](/Java/JComboBox/insertItemAt)
* [installAncestorListener()](/Java/JComboBox/installAncestorListener)
* [intervalAdded()](/Java/JComboBox/intervalAdded)
* [intervalRemoved()](/Java/JComboBox/intervalRemoved)
* [isEditable()](/Java/JComboBox/isEditable)
* [isLightWeightPopupEnabled()](/Java/JComboBox/isLightWeightPopupEnabled)
* [isPopupVisible()](/Java/JComboBox/isPopupVisible)
* [paramString()](/Java/JComboBox/paramString)
* [processKeyEvent()](/Java/JComboBox/processKeyEvent)
* [removeActionListener()](/Java/JComboBox/removeActionListener)
* [removeAllItems()](/Java/JComboBox/removeAllItems)
* [removeItem()](/Java/JComboBox/removeItem)
* [removeItemAt()](/Java/JComboBox/removeItemAt)
* [removeItemListener()](/Java/JComboBox/removeItemListener)
* [removePopupMenuListener()](/Java/JComboBox/removePopupMenuListener)
* [selectedItemChanged()](/Java/JComboBox/selectedItemChanged)
* [selectWithKeyChar()](/Java/JComboBox/selectWithKeyChar)
* [setAction()](/Java/JComboBox/setAction)
* [setActionCommand()](/Java/JComboBox/setActionCommand)
* [setEditable()](/Java/JComboBox/setEditable)
* [setEditor()](/Java/JComboBox/setEditor)
* [setEnabled()](/Java/JComboBox/setEnabled)
* [setKeySelectionManager()](/Java/JComboBox/setKeySelectionManager)
* [setLightWeightPopupEnabled()](/Java/JComboBox/setLightWeightPopupEnabled)
* [setMaximumRowCount()](/Java/JComboBox/setMaximumRowCount)
* [setModel()](/Java/JComboBox/setModel)
* [setPopupVisible()](/Java/JComboBox/setPopupVisible)
* [setPrototypeDisplayValue()](/Java/JComboBox/setPrototypeDisplayValue)
* [setRenderer()](/Java/JComboBox/setRenderer)
* [setSelectedIndex()](/Java/JComboBox/setSelectedIndex)
* [setSelectedItem()](/Java/JComboBox/setSelectedItem)
* [setUI()](/Java/JComboBox/setUI)
* [showPopup()](/Java/JComboBox/showPopup)
* [updateUI()](/Java/JComboBox/updateUI)

## Ejemplo
~~~java
{{ site.data.Java.J.JComboBox.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JComboBox.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
