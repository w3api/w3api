---
title: PortableRemoteObjectDelegate.unexportObject()
permalink: /Java/PortableRemoteObjectDelegate/unexportObject/
date: 2021-01-11
key: Java.P.PortableRemoteObjectDelegate
category: Java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PortableRemoteObjectDelegate.metodos valor="unexportObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void unexportObject(Remote obj) throws NoSuchObjectException
~~~

## Parámetros
* **Remote obj**,  {% include w3api/param_description.html metodo=_dato parametro="Remote obj" %}

## Excepciones
[NoSuchObjectException](/Java/NoSuchObjectException/)

## Clase Padre
[PortableRemoteObjectDelegate](/Java/PortableRemoteObjectDelegate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
