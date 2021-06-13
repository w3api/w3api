---
title: ObjectOutputStream.enableReplaceObject()
permalink: /Java/ObjectOutputStream/enableReplaceObject/
date: 2021-01-11
key: Java.O.ObjectOutputStream
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectOutputStream.metodos valor="enableReplaceObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected boolean enableReplaceObject(boolean enable) throws SecurityException
~~~

## Parámetros
* **boolean enable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean enable" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[ObjectOutputStream](/Java/ObjectOutputStream/)

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
