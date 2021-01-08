---
title: HttpsServer.setHttpsConfigurator()
permalink: Java/HttpsServer/setHttpsConfigurator
date: 2021-01-04
key: JavaJava.H.HttpsServer
category: java
tags: ['java se', 'com.sun.net.httpserver', 'jdk.httpserver', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpsServer.metodos valor="setHttpsConfigurator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setHttpsConfigurator(HttpsConfigurator config)
~~~

## Parámetros
* **HttpsConfigurator config**,  {% include w3api/param_description.html metodo=_data parametro="HttpsConfigurator config" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[HttpsServer](/Java/HttpsServer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpsServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
