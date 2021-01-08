---
title: ServantLocatorOperations.preinvoke()
permalink: Java/ServantLocatorOperations/preinvoke
date: 2021-01-04
key: JavaJava.S.ServantLocatorOperations
category: java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServantLocatorOperations.metodos valor="preinvoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Servant preinvoke(byte[] oid, POA adapter, String operation, CookieHolder the_cookie) throws ForwardRequest
~~~

## Parámetros
* **byte[] oid**,  {% include w3api/param_description.html metodo=_data parametro="byte[] oid" %}
* **POA adapter**,  {% include w3api/param_description.html metodo=_data parametro="POA adapter" %}
* **String operation**,  {% include w3api/param_description.html metodo=_data parametro="String operation" %}
* **CookieHolder the_cookie**,  {% include w3api/param_description.html metodo=_data parametro="CookieHolder the_cookie" %}

## Clase Padre
[ServantLocatorOperations](/Java/ServantLocatorOperations/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServantLocatorOperations.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
