---
title: UtilDelegate.writeAbstractObject()
permalink: /Java/UtilDelegate/writeAbstractObject/
date: 2021-01-11
key: Java.U.UtilDelegate
category: Java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UtilDelegate.metodos valor="writeAbstractObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeAbstractObject(OutputStream out, Object obj)
~~~

## Parámetros
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}

## Excepciones
[NoSuchObjectException](/Java/NoSuchObjectException/)

## Clase Padre
[UtilDelegate](/Java/UtilDelegate/)

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
