---
title: AWTEventMulticaster.add()
permalink: /Java/AWTEventMulticaster/add/
date: 2021-01-11
key: Java.A.AWTEventMulticaster
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AWTEventMulticaster.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ActionListener add(ActionListener a, ActionListener b)
public static AdjustmentListener add(AdjustmentListener a, AdjustmentListener b)
public static ComponentListener add(ComponentListener a, ComponentListener b)
public static ContainerListener add(ContainerListener a, ContainerListener b)
public static FocusListener add(FocusListener a, FocusListener b)
public static HierarchyBoundsListener add(HierarchyBoundsListener a, HierarchyBoundsListener b)
public static HierarchyListener add(HierarchyListener a, HierarchyListener b)
public static InputMethodListener add(InputMethodListener a, InputMethodListener b)
public static ItemListener add(ItemListener a, ItemListener b)
public static KeyListener add(KeyListener a, KeyListener b)
public static MouseListener add(MouseListener a, MouseListener b)
public static MouseMotionListener add(MouseMotionListener a, MouseMotionListener b)
public static MouseWheelListener add(MouseWheelListener a, MouseWheelListener b)
public static TextListener add(TextListener a, TextListener b)
public static WindowFocusListener add(WindowFocusListener a, WindowFocusListener b)
public static WindowListener add(WindowListener a, WindowListener b)
public static WindowStateListener add(WindowStateListener a, WindowStateListener b)
~~~

## Parámetros
* **MouseListener b**,  {% include w3api/param_description.html metodo=_dato parametro="MouseListener b" %}
* **MouseWheelListener b**,  {% include w3api/param_description.html metodo=_dato parametro="MouseWheelListener b" %}
* **AdjustmentListener a**,  {% include w3api/param_description.html metodo=_dato parametro="AdjustmentListener a" %}
* **InputMethodListener b**,  {% include w3api/param_description.html metodo=_dato parametro="InputMethodListener b" %}
* **ItemListener b**,  {% include w3api/param_description.html metodo=_dato parametro="ItemListener b" %}
* **ComponentListener a**,  {% include w3api/param_description.html metodo=_dato parametro="ComponentListener a" %}
* **WindowListener a**,  {% include w3api/param_description.html metodo=_dato parametro="WindowListener a" %}
* **WindowStateListener b**,  {% include w3api/param_description.html metodo=_dato parametro="WindowStateListener b" %}
* **ActionListener b**,  {% include w3api/param_description.html metodo=_dato parametro="ActionListener b" %}
* **ItemListener a**,  {% include w3api/param_description.html metodo=_dato parametro="ItemListener a" %}
* **AdjustmentListener b**,  {% include w3api/param_description.html metodo=_dato parametro="AdjustmentListener b" %}
* **TextListener a**,  {% include w3api/param_description.html metodo=_dato parametro="TextListener a" %}
* **KeyListener a**,  {% include w3api/param_description.html metodo=_dato parametro="KeyListener a" %}
* **ActionListener a**,  {% include w3api/param_description.html metodo=_dato parametro="ActionListener a" %}
* **FocusListener b**,  {% include w3api/param_description.html metodo=_dato parametro="FocusListener b" %}
* **HierarchyBoundsListener a**,  {% include w3api/param_description.html metodo=_dato parametro="HierarchyBoundsListener a" %}
* **MouseMotionListener b**,  {% include w3api/param_description.html metodo=_dato parametro="MouseMotionListener b" %}
* **WindowFocusListener b**,  {% include w3api/param_description.html metodo=_dato parametro="WindowFocusListener b" %}
* **ContainerListener a**,  {% include w3api/param_description.html metodo=_dato parametro="ContainerListener a" %}
* **MouseWheelListener a**,  {% include w3api/param_description.html metodo=_dato parametro="MouseWheelListener a" %}
* **WindowFocusListener a**,  {% include w3api/param_description.html metodo=_dato parametro="WindowFocusListener a" %}
* **FocusListener a**,  {% include w3api/param_description.html metodo=_dato parametro="FocusListener a" %}
* **MouseListener a**,  {% include w3api/param_description.html metodo=_dato parametro="MouseListener a" %}
* **HierarchyListener a**,  {% include w3api/param_description.html metodo=_dato parametro="HierarchyListener a" %}
* **KeyListener b**,  {% include w3api/param_description.html metodo=_dato parametro="KeyListener b" %}
* **MouseMotionListener a**,  {% include w3api/param_description.html metodo=_dato parametro="MouseMotionListener a" %}
* **ContainerListener b**,  {% include w3api/param_description.html metodo=_dato parametro="ContainerListener b" %}
* **TextListener b**,  {% include w3api/param_description.html metodo=_dato parametro="TextListener b" %}
* **WindowListener b**,  {% include w3api/param_description.html metodo=_dato parametro="WindowListener b" %}
* **WindowStateListener a**,  {% include w3api/param_description.html metodo=_dato parametro="WindowStateListener a" %}
* **HierarchyBoundsListener b**,  {% include w3api/param_description.html metodo=_dato parametro="HierarchyBoundsListener b" %}
* **ComponentListener b**,  {% include w3api/param_description.html metodo=_dato parametro="ComponentListener b" %}
* **HierarchyListener b**,  {% include w3api/param_description.html metodo=_dato parametro="HierarchyListener b" %}
* **InputMethodListener a**,  {% include w3api/param_description.html metodo=_dato parametro="InputMethodListener a" %}

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
