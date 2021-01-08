---
title: RMISocketFactory.createServerSocket()
permalink: Java/RMISocketFactory/createServerSocket
date: 2021-01-04
key: JavaJava.R.RMISocketFactory
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMISocketFactory.metodos valor="createServerSocket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract ServerSocket createServerSocket(int port) throws IOException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}

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
{%- for _ldc in site.data.Java.R.RMISocketFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
