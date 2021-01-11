---
title: PortableRemoteObject.unexportObject()
permalink: Java/PortableRemoteObject/unexportObject
date: 2021-01-11
key: JavaJava.P.PortableRemoteObject
category: java
tags: ['java se', 'javax.rmi', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PortableRemoteObject.metodos valor="unexportObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void unexportObject(Remote obj) throws NoSuchObjectException
~~~

## Parámetros
* **Remote obj**,  {% include w3api/param_description.html metodo=_dato parametro="Remote obj" %}

## Excepciones
[NoSuchObjectException](/Java/NoSuchObjectException/)

## Clase Padre
[PortableRemoteObject](/Java/PortableRemoteObject/)

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
