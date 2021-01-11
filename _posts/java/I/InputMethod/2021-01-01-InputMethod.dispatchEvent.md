---
title: InputMethod.dispatchEvent()
permalink: Java/InputMethod/dispatchEvent
date: 2021-01-11
key: JavaJava.I.InputMethod
category: java
tags: ['java se', 'java.awt.im.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputMethod.metodos valor="dispatchEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void dispatchEvent(AWTEvent event)
~~~

## Parámetros
* **AWTEvent event**,  {% include w3api/param_description.html metodo=_dato parametro="AWTEvent event" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[InputMethod](/Java/InputMethod/)

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
