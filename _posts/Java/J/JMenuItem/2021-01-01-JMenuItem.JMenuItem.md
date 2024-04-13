---
title: JMenuItem.JMenuItem()
permalink: /Java/JMenuItem/JMenuItem/
date: 2021-01-11
key: Java.J.JMenuItem
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMenuItem.constructores valor="JMenuItem" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JMenuItem()
public JMenuItem(String text)
public JMenuItem(String text, int mnemonic)
public JMenuItem(String text, Icon icon)
public JMenuItem(Action a)
public JMenuItem(Icon icon)
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **Action a**,  {% include w3api/param_description.html metodo=_dato parametro="Action a" %}
* **int mnemonic**,  {% include w3api/param_description.html metodo=_dato parametro="int mnemonic" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}

## Clase Padre
[JMenuItem](/Java/JMenuItem/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
