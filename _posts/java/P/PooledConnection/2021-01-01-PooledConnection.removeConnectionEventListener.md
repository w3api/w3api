---
title: PooledConnection.removeConnectionEventListener()
permalink: /Java/PooledConnection/removeConnectionEventListener/
date: 2021-01-11
key: Java.P.PooledConnection
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PooledConnection.metodos valor="removeConnectionEventListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeConnectionEventListener(ConnectionEventListener listener)
~~~

## Parámetros
* **ConnectionEventListener listener**,  {% include w3api/param_description.html metodo=_dato parametro="ConnectionEventListener listener" %}

## Clase Padre
[PooledConnection](/Java/PooledConnection/)

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
