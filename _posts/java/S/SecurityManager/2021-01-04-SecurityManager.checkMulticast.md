---
title: SecurityManager.checkMulticast()
permalink: Java/SecurityManager/checkMulticast
date: 2021-01-04
key: JavaJava.S.SecurityManager
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecurityManager.metodos valor="checkMulticast" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void checkMulticast(InetAddress maddr)
@Deprecated(since="1.4") public void checkMulticast(InetAddress maddr, byte ttl)
~~~

## Parámetros
* **InetAddress maddr**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress maddr" %}
* **byte ttl**,  {% include w3api/param_description.html metodo=_data parametro="byte ttl" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SecurityManager](/Java/SecurityManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecurityManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
