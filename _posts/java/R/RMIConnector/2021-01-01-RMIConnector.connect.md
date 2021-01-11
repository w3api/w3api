---
title: RMIConnector.connect()
permalink: Java/RMIConnector/connect
date: 2021-01-11
key: JavaJava.R.RMIConnector
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnector.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void connect() throws IOException
public void connect(Map<String,?> environment) throws IOException
~~~

## Parámetros
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[RMIConnector](/Java/RMIConnector/)

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
