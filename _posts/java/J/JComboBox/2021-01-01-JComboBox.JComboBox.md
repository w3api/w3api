---
title: JComboBox.JComboBox()
permalink: /Java/JComboBox/JComboBox/
date: 2021-01-11
key: Java.J.JComboBox
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComboBox.constructores valor="JComboBox" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JComboBox()
public JComboBox(E[] items)
public JComboBox(Vector<E> items)
public JComboBox(ComboBoxModel<E> aModel)
~~~

## Parámetros
* **E[] items**,  {% include w3api/param_description.html metodo=_dato parametro="E[] items" %}
* **ComboBoxModel&lt;E&gt; aModel**,  {% include w3api/param_description.html metodo=_dato parametro="ComboBoxModel<E> aModel" %}
* **Vector&lt;E&gt; items**,  {% include w3api/param_description.html metodo=_dato parametro="Vector<E> items" %}

## Clase Padre
[JComboBox](/Java/JComboBox/)

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
