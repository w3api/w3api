---
title: AWTEventMulticaster.add()
permalink: Java/AWTEventMulticaster/add
date: 2021-01-10
key: JavaJava.A.AWTEventMulticaster
category: java
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
* **WindowStateListener b**,  {% include w3api/param_description.html metodo=_dato parametro="WindowStateListener b" %}
* **KeyListener b**,  {% include w3api/param_description.html metodo=_dato parametro="KeyListener b" %}
* **MouseMotionListener b**,  {% include w3api/param_description.html metodo=_dato parametro="MouseMotionListener b" %}
* **WindowListener a**,  {% include w3api/param_description.html metodo=_dato parametro="WindowListener a" %}
* **WindowStateListener a**,  {% include w3api/param_description.html metodo=_dato parametro="WindowStateListener a" %}
* **ComponentListener a**,  {% include w3api/param_description.html metodo=_dato parametro="ComponentListener a" %}
* **KeyListener a**,  {% include w3api/param_description.html metodo=_dato parametro="KeyListener a" %}
* **HierarchyListener a**,  {% include w3api/param_description.html metodo=_dato parametro="HierarchyListener a" %}
* **WindowFocusListener a**,  {% include w3api/param_description.html metodo=_dato parametro="WindowFocusListener a" %}
* **ContainerListener b**,  {% include w3api/param_description.html metodo=_dato parametro="ContainerListener b" %}
* **HierarchyListener b**,  {% include w3api/param_description.html metodo=_dato parametro="HierarchyListener b" %}
* **ItemListener b**,  {% include w3api/param_description.html metodo=_dato parametro="ItemListener b" %}
* **ActionListener b**,  {% include w3api/param_description.html metodo=_dato parametro="ActionListener b" %}
* **WindowListener b**,  {% include w3api/param_description.html metodo=_dato parametro="WindowListener b" %}
* **MouseWheelListener b**,  {% include w3api/param_description.html metodo=_dato parametro="MouseWheelListener b" %}
* **InputMethodListener b**,  {% include w3api/param_description.html metodo=_dato parametro="InputMethodListener b" %}
* **MouseWheelListener a**,  {% include w3api/param_description.html metodo=_dato parametro="MouseWheelListener a" %}
* **MouseMotionListener a**,  {% include w3api/param_description.html metodo=_dato parametro="MouseMotionListener a" %}
* **AdjustmentListener b**,  {% include w3api/param_description.html metodo=_dato parametro="AdjustmentListener b" %}
* **AdjustmentListener a**,  {% include w3api/param_description.html metodo=_dato parametro="AdjustmentListener a" %}
* **WindowFocusListener b**,  {% include w3api/param_description.html metodo=_dato parametro="WindowFocusListener b" %}
* **ItemListener a**,  {% include w3api/param_description.html metodo=_dato parametro="ItemListener a" %}
* **FocusListener b**,  {% include w3api/param_description.html metodo=_dato parametro="FocusListener b" %}
* **ActionListener a**,  {% include w3api/param_description.html metodo=_dato parametro="ActionListener a" %}
* **InputMethodListener a**,  {% include w3api/param_description.html metodo=_dato parametro="InputMethodListener a" %}
* **FocusListener a**,  {% include w3api/param_description.html metodo=_dato parametro="FocusListener a" %}
* **MouseListener b**,  {% include w3api/param_description.html metodo=_dato parametro="MouseListener b" %}
* **HierarchyBoundsListener a**,  {% include w3api/param_description.html metodo=_dato parametro="HierarchyBoundsListener a" %}
* **ComponentListener b**,  {% include w3api/param_description.html metodo=_dato parametro="ComponentListener b" %}
* **ContainerListener a**,  {% include w3api/param_description.html metodo=_dato parametro="ContainerListener a" %}
* **TextListener b**,  {% include w3api/param_description.html metodo=_dato parametro="TextListener b" %}
* **HierarchyBoundsListener b**,  {% include w3api/param_description.html metodo=_dato parametro="HierarchyBoundsListener b" %}
* **MouseListener a**,  {% include w3api/param_description.html metodo=_dato parametro="MouseListener a" %}
* **TextListener a**,  {% include w3api/param_description.html metodo=_dato parametro="TextListener a" %}

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
