---
title: RMIClientSocketFactory.createSocket()
permalink: /Java/RMIClientSocketFactory/createSocket/
date: 2021-01-11
key: Java.R.RMIClientSocketFactory
category: Java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIClientSocketFactory.metodos valor="createSocket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Socket createSocket(String host, int port) throws IOException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[RMIClientSocketFactory](/Java/RMIClientSocketFactory/)

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
