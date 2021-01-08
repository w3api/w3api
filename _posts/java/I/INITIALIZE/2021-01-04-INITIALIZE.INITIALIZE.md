---
title: INITIALIZE.INITIALIZE()
permalink: Java/INITIALIZE/INITIALIZE
date: 2021-01-04
key: JavaJava.I.INITIALIZE
category: java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'JDKJava 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.INITIALIZE.constructores valor="INITIALIZE" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public INITIALIZE()
public INITIALIZE(int minor, CompletionStatus completed)
public INITIALIZE(String s)
public INITIALIZE(String s, int minor, CompletionStatus completed)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}
* **int minor**,  {% include w3api/param_description.html metodo=_data parametro="int minor" %}
* **CompletionStatus completed**,  {% include w3api/param_description.html metodo=_data parametro="CompletionStatus completed" %}

## Clase Padre
[INITIALIZE](/Java/INITIALIZE/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.INITIALIZE.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
