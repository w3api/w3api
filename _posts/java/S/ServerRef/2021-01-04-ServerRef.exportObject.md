---
title: ServerRef.exportObject()
permalink: Java/ServerRef/exportObject
date: 2021-01-04
key: JavaJava.S.ServerRef
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServerRef.metodos valor="exportObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
RemoteStub exportObject(Remote obj, Object data) throws RemoteException
~~~

## Parámetros
* **Object data**,  {% include w3api/param_description.html metodo=_data parametro="Object data" %}
* **Remote obj**,  {% include w3api/param_description.html metodo=_data parametro="Remote obj" %}

## Excepciones
[RemoteException](/Java/RemoteException/)

## Clase Padre
[ServerRef](/Java/ServerRef/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServerRef.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
