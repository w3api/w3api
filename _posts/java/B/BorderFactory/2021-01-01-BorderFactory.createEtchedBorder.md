---
title: BorderFactory.createEtchedBorder()
permalink: Java/BorderFactory/createEtchedBorder
date: 2021-01-11
key: JavaJava.B.BorderFactory
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BorderFactory.metodos valor="createEtchedBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Border createEtchedBorder()
public static Border createEtchedBorder(int type)
public static Border createEtchedBorder(int type, Color highlight, Color shadow)
public static Border createEtchedBorder(Color highlight, Color shadow)
~~~

## Parámetros
* **Color shadow**,  {% include w3api/param_description.html metodo=_dato parametro="Color shadow" %}
* **Color highlight**,  {% include w3api/param_description.html metodo=_dato parametro="Color highlight" %}
* **int type**,  {% include w3api/param_description.html metodo=_dato parametro="int type" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BorderFactory](/Java/BorderFactory/)

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
