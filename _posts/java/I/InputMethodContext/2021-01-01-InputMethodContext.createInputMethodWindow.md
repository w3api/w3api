---
title: InputMethodContext.createInputMethodWindow()
permalink: /Java/InputMethodContext/createInputMethodWindow/
date: 2021-01-11
key: Java.I.InputMethodContext
category: Java
tags: ['java se', 'java.awt.im.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputMethodContext.metodos valor="createInputMethodWindow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Window createInputMethodWindow(String title, boolean attachToInputContext)
~~~

## Parámetros
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **boolean attachToInputContext**,  {% include w3api/param_description.html metodo=_dato parametro="boolean attachToInputContext" %}

## Excepciones
[HeadlessException](/Java/HeadlessException/)

## Clase Padre
[InputMethodContext](/Java/InputMethodContext/)

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
