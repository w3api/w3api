---
title: RMIServerImpl.closeClient()
permalink: Java/RMIServerImpl/closeClient
date: 2021-01-04
key: JavaJava.R.RMIServerImpl
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIServerImpl.metodos valor="closeClient" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void closeClient(RMIConnection client) throws IOException
~~~

## Parámetros
* **RMIConnection client**,  {% include w3api/param_description.html metodo=_data parametro="RMIConnection client" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[RMIServerImpl](/Java/RMIServerImpl/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RMIServerImpl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
