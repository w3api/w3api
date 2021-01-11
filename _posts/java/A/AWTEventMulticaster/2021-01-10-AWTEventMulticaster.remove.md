---
title: AWTEventMulticaster.remove()
permalink: Java/AWTEventMulticaster/remove
date: 2021-01-10
key: JavaJava.A.AWTEventMulticaster
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AWTEventMulticaster.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ActionListener remove(ActionListener l, ActionListener oldl)
public static AdjustmentListener remove(AdjustmentListener l, AdjustmentListener oldl)
public static ComponentListener remove(ComponentListener l, ComponentListener oldl)
public static ContainerListener remove(ContainerListener l, ContainerListener oldl)
public static FocusListener remove(FocusListener l, FocusListener oldl)
public static HierarchyBoundsListener remove(HierarchyBoundsListener l, HierarchyBoundsListener oldl)
public static HierarchyListener remove(HierarchyListener l, HierarchyListener oldl)
public static InputMethodListener remove(InputMethodListener l, InputMethodListener oldl)
public static ItemListener remove(ItemListener l, ItemListener oldl)
public static KeyListener remove(KeyListener l, KeyListener oldl)
public static MouseListener remove(MouseListener l, MouseListener oldl)
public static MouseMotionListener remove(MouseMotionListener l, MouseMotionListener oldl)
public static MouseWheelListener remove(MouseWheelListener l, MouseWheelListener oldl)
public static TextListener remove(TextListener l, TextListener oldl)
public static WindowFocusListener remove(WindowFocusListener l, WindowFocusListener oldl)
public static WindowListener remove(WindowListener l, WindowListener oldl)
public static WindowStateListener remove(WindowStateListener l, WindowStateListener oldl)
protected EventListener remove(EventListener oldl)
~~~

## Parámetros
* **MouseListener l**,  {% include w3api/param_description.html metodo=_dato parametro="MouseListener l" %}
* **ActionListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="ActionListener oldl" %}
* **FocusListener l**,  {% include w3api/param_description.html metodo=_dato parametro="FocusListener l" %}
* **KeyListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="KeyListener oldl" %}
* **HierarchyListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="HierarchyListener oldl" %}
* **TextListener l**,  {% include w3api/param_description.html metodo=_dato parametro="TextListener l" %}
* **ContainerListener l**,  {% include w3api/param_description.html metodo=_dato parametro="ContainerListener l" %}
* **FocusListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="FocusListener oldl" %}
* **AdjustmentListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="AdjustmentListener oldl" %}
* **TextListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="TextListener oldl" %}
* **MouseWheelListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="MouseWheelListener oldl" %}
* **WindowListener l**,  {% include w3api/param_description.html metodo=_dato parametro="WindowListener l" %}
* **WindowFocusListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="WindowFocusListener oldl" %}
* **ComponentListener l**,  {% include w3api/param_description.html metodo=_dato parametro="ComponentListener l" %}
* **InputMethodListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="InputMethodListener oldl" %}
* **WindowListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="WindowListener oldl" %}
* **WindowFocusListener l**,  {% include w3api/param_description.html metodo=_dato parametro="WindowFocusListener l" %}
* **HierarchyBoundsListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="HierarchyBoundsListener oldl" %}
* **MouseMotionListener l**,  {% include w3api/param_description.html metodo=_dato parametro="MouseMotionListener l" %}
* **WindowStateListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="WindowStateListener oldl" %}
* **WindowStateListener l**,  {% include w3api/param_description.html metodo=_dato parametro="WindowStateListener l" %}
* **KeyListener l**,  {% include w3api/param_description.html metodo=_dato parametro="KeyListener l" %}
* **ItemListener l**,  {% include w3api/param_description.html metodo=_dato parametro="ItemListener l" %}
* **MouseWheelListener l**,  {% include w3api/param_description.html metodo=_dato parametro="MouseWheelListener l" %}
* **ContainerListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="ContainerListener oldl" %}
* **ItemListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="ItemListener oldl" %}
* **MouseMotionListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="MouseMotionListener oldl" %}
* **EventListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="EventListener oldl" %}
* **InputMethodListener l**,  {% include w3api/param_description.html metodo=_dato parametro="InputMethodListener l" %}
* **HierarchyListener l**,  {% include w3api/param_description.html metodo=_dato parametro="HierarchyListener l" %}
* **ActionListener l**,  {% include w3api/param_description.html metodo=_dato parametro="ActionListener l" %}
* **AdjustmentListener l**,  {% include w3api/param_description.html metodo=_dato parametro="AdjustmentListener l" %}
* **ComponentListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="ComponentListener oldl" %}
* **HierarchyBoundsListener l**,  {% include w3api/param_description.html metodo=_dato parametro="HierarchyBoundsListener l" %}
* **MouseListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="MouseListener oldl" %}

## Clase Padre
[AWTEventMulticaster](/Java/AWTEventMulticaster/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
