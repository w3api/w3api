---
title: NetworkPermission.NetworkPermission()
permalink: Java/NetworkPermission/NetworkPermission
date: 2021-01-11
key: JavaJava.N.NetworkPermission
category: java
tags: ['java se', 'jdk.net', 'jdk.net', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NetworkPermission.constructores valor="NetworkPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public NetworkPermission(String name)
public NetworkPermission(String name, String actions)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[NetworkPermission](/Java/NetworkPermission/)

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
