---
title: PortableRemoteObject.exportObject()
permalink: /Java/PortableRemoteObject/exportObject/
date: 2021-01-11
key: Java.P.PortableRemoteObject
category: Java
tags: ['java se', 'javax.rmi', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PortableRemoteObject.metodos valor="exportObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void exportObject(Remote obj) throws RemoteException
~~~

## Parámetros
* **Remote obj**,  {% include w3api/param_description.html metodo=_dato parametro="Remote obj" %}

## Excepciones
[RemoteException](/Java/RemoteException/)

## Clase Padre
[PortableRemoteObject](/Java/PortableRemoteObject/)

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
