---
title: ServerRef.getClientHost()
permalink: /Java/ServerRef/getClientHost/
date: 2021-01-11
key: Java.S.ServerRef
category: Java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServerRef.metodos valor="getClientHost" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String getClientHost() throws ServerNotActiveException
~~~

## Excepciones
[ServerNotActiveException](/Java/ServerNotActiveException/)

## Clase Padre
[ServerRef](/Java/ServerRef/)

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
