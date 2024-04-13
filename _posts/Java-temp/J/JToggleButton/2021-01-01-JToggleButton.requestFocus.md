---
title: JToggleButton.requestFocus()
permalink: /Java/JToggleButton/requestFocus/
date: 2021-01-11
key: Java.J.JToggleButton
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JToggleButton.metodos valor="requestFocus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void requestFocus(FocusEvent.Cause cause)
~~~

## Parámetros
* **FocusEvent.Cause cause**,  {% include w3api/param_description.html metodo=_dato parametro="FocusEvent.Cause cause" %}

## Clase Padre
[JToggleButton](/Java/JToggleButton/)

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
