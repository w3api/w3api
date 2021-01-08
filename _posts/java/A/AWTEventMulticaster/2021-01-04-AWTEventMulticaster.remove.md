---
title: AWTEventMulticaster.remove()
permalink: Java/AWTEventMulticaster/remove
date: 2021-01-04
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
* **InputMethodListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="InputMethodListener oldl" %}
* **MouseListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="MouseListener oldl" %}
* **MouseWheelListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="MouseWheelListener oldl" %}
* **TextListener l**,  {% include w3api/param_description.html metodo=_data parametro="TextListener l" %}
* **EventListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="EventListener oldl" %}
* **MouseMotionListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="MouseMotionListener oldl" %}
* **KeyListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="KeyListener oldl" %}
* **WindowFocusListener l**,  {% include w3api/param_description.html metodo=_data parametro="WindowFocusListener l" %}
* **ComponentListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="ComponentListener oldl" %}
* **AdjustmentListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="AdjustmentListener oldl" %}
* **HierarchyListener l**,  {% include w3api/param_description.html metodo=_data parametro="HierarchyListener l" %}
* **ContainerListener l**,  {% include w3api/param_description.html metodo=_data parametro="ContainerListener l" %}
* **InputMethodListener l**,  {% include w3api/param_description.html metodo=_data parametro="InputMethodListener l" %}
* **AdjustmentListener l**,  {% include w3api/param_description.html metodo=_data parametro="AdjustmentListener l" %}
* **KeyListener l**,  {% include w3api/param_description.html metodo=_data parametro="KeyListener l" %}
* **WindowStateListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="WindowStateListener oldl" %}
* **ActionListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="ActionListener oldl" %}
* **WindowFocusListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="WindowFocusListener oldl" %}
* **MouseListener l**,  {% include w3api/param_description.html metodo=_data parametro="MouseListener l" %}
* **FocusListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="FocusListener oldl" %}
* **ItemListener l**,  {% include w3api/param_description.html metodo=_data parametro="ItemListener l" %}
* **ComponentListener l**,  {% include w3api/param_description.html metodo=_data parametro="ComponentListener l" %}
* **WindowListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="WindowListener oldl" %}
* **HierarchyListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="HierarchyListener oldl" %}
* **ItemListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="ItemListener oldl" %}
* **MouseMotionListener l**,  {% include w3api/param_description.html metodo=_data parametro="MouseMotionListener l" %}
* **TextListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="TextListener oldl" %}
* **ActionListener l**,  {% include w3api/param_description.html metodo=_data parametro="ActionListener l" %}
* **WindowStateListener l**,  {% include w3api/param_description.html metodo=_data parametro="WindowStateListener l" %}
* **FocusListener l**,  {% include w3api/param_description.html metodo=_data parametro="FocusListener l" %}
* **HierarchyBoundsListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="HierarchyBoundsListener oldl" %}
* **ContainerListener oldl**,  {% include w3api/param_description.html metodo=_data parametro="ContainerListener oldl" %}
* **HierarchyBoundsListener l**,  {% include w3api/param_description.html metodo=_data parametro="HierarchyBoundsListener l" %}
* **MouseWheelListener l**,  {% include w3api/param_description.html metodo=_data parametro="MouseWheelListener l" %}
* **WindowListener l**,  {% include w3api/param_description.html metodo=_data parametro="WindowListener l" %}

## Clase Padre
[AWTEventMulticaster](/Java/AWTEventMulticaster/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AWTEventMulticaster.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
