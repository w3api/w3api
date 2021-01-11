---
title: RMIServerImpl.newClient()
permalink: Java/RMIServerImpl/newClient
date: 2021-01-11
key: JavaJava.R.RMIServerImpl
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIServerImpl.metodos valor="newClient" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RMIConnection newClient(Object credentials) throws IOException
~~~

## Parámetros
* **Object credentials**,  {% include w3api/param_description.html metodo=_dato parametro="Object credentials" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

## Clase Padre
[RMIServerImpl](/Java/RMIServerImpl/)

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
