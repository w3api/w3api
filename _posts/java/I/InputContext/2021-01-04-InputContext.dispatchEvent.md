---
title: InputContext.dispatchEvent()
permalink: Java/InputContext/dispatchEvent
date: 2021-01-04
key: JavaJava.I.InputContext
category: java
tags: ['java se', 'java.awt.im', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputContext.metodos valor="dispatchEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void dispatchEvent(AWTEvent event)
~~~

## Parámetros
* **AWTEvent event**,  {% include w3api/param_description.html metodo=_data parametro="AWTEvent event" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[InputContext](/Java/InputContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InputContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
