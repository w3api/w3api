---
title: RMISocketFactory.createSocket()
permalink: Java/RMISocketFactory/createSocket
date: 2021-01-11
key: JavaJava.R.RMISocketFactory
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMISocketFactory.metodos valor="createSocket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Socket createSocket(String host, int port) throws IOException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[RMISocketFactory](/Java/RMISocketFactory/)

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
