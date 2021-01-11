---
title: UtilDelegate.loadClass()
permalink: Java/UtilDelegate/loadClass
date: 2021-01-11
key: JavaJava.U.UtilDelegate
category: java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UtilDelegate.metodos valor="loadClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Class loadClass(String className, String remoteCodebase, ClassLoader loader) throws ClassNotFoundException
~~~

## Parámetros
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader loader" %}
* **String remoteCodebase**,  {% include w3api/param_description.html metodo=_dato parametro="String remoteCodebase" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/)

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
