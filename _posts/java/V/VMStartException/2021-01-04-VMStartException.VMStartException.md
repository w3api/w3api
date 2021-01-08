---
title: VMStartException.VMStartException()
permalink: Java/VMStartException/VMStartException
date: 2021-01-04
key: JavaJava.V.VMStartException
category: java
tags: ['java se', 'com.sun.jdi.connect', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VMStartException.constructores valor="VMStartException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public VMStartException(Process process)
public VMStartException(String message, Process process)
~~~

## Parámetros
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **Process process**,  {% include w3api/param_description.html metodo=_data parametro="Process process" %}

## Clase Padre
[VMStartException](/Java/VMStartException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.VMStartException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
