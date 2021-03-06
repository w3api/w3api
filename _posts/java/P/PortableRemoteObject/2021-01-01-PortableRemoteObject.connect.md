---
title: PortableRemoteObject.connect()
permalink: /Java/PortableRemoteObject/connect/
date: 2021-01-11
key: Java.P.PortableRemoteObject
category: Java
tags: ['java se', 'javax.rmi', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PortableRemoteObject.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void connect(Remote target, Remote source) throws RemoteException
~~~

## Parámetros
* **Remote source**,  {% include w3api/param_description.html metodo=_dato parametro="Remote source" %}
* **Remote target**,  {% include w3api/param_description.html metodo=_dato parametro="Remote target" %}

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
