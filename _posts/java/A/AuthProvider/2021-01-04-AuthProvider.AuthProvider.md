---
title: AuthProvider.AuthProvider()
permalink: Java/AuthProvider/AuthProvider
date: 2021-01-04
key: JavaJava.A.AuthProvider
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AuthProvider.constructores valor="AuthProvider" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="9") protected AuthProvider(String name, double version, String info)
protected AuthProvider(String name, String versionStr, String info)
~~~

## Parámetros
* **String versionStr**,  {% include w3api/param_description.html metodo=_data parametro="String versionStr" %}
* **String info**,  {% include w3api/param_description.html metodo=_data parametro="String info" %}
* **double version**,  {% include w3api/param_description.html metodo=_data parametro="double version" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Clase Padre
[AuthProvider](/Java/AuthProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AuthProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
