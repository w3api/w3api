---
title: Reference.Reference()
permalink: Java/Reference-javax-naming/Reference
date: 2021-01-11
key: JavaJava.R.Reference-javax-naming
category: java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.Reference-javax-naming.constructores valor="Reference" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Reference(String className)
public Reference(String className, String factory, String factoryLocation)
public Reference(String className, RefAddr addr)
public Reference(String className, RefAddr addr, String factory, String factoryLocation)
~~~

## Parámetros
* **String factoryLocation**,  {% include w3api/param_description.html metodo=_dato parametro="String factoryLocation" %}
* **RefAddr addr**,  {% include w3api/param_description.html metodo=_dato parametro="RefAddr addr" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}
* **String factory**,  {% include w3api/param_description.html metodo=_dato parametro="String factory" %}

## Clase Padre
[Reference](/Java/Reference-javax-naming/)

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
