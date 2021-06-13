---
title: RemoteServer.setLog()
permalink: /Java/RemoteServer/setLog/
date: 2021-01-11
key: Java.R.RemoteServer
category: Java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RemoteServer.metodos valor="setLog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setLog(OutputStream out)
~~~

## Parámetros
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[RemoteServer](/Java/RemoteServer/)

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
