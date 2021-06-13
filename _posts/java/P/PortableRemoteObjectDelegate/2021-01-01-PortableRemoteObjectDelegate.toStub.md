---
title: PortableRemoteObjectDelegate.toStub()
permalink: /Java/PortableRemoteObjectDelegate/toStub/
date: 2021-01-11
key: Java.P.PortableRemoteObjectDelegate
category: java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PortableRemoteObjectDelegate.metodos valor="toStub" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Remote toStub(Remote obj) throws NoSuchObjectException
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

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
