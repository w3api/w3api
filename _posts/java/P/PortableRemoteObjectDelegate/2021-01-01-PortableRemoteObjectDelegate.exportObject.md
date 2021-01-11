---
title: PortableRemoteObjectDelegate.exportObject()
permalink: Java/PortableRemoteObjectDelegate/exportObject
date: 2021-01-11
key: JavaJava.P.PortableRemoteObjectDelegate
category: java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PortableRemoteObjectDelegate.metodos valor="exportObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void exportObject(Remote obj) throws RemoteException
~~~

## Parámetros
* **Remote obj**,  {% include w3api/param_description.html metodo=_dato parametro="Remote obj" %}

## Excepciones
[RemoteException](/Java/RemoteException/)

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
