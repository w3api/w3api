---
title: _ServantLocatorStub.preinvoke()
permalink: /Java/_ServantLocatorStub/preinvoke/
date: 2021-01-11
key: JavaJava._._ServantLocatorStub
category: java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java._._ServantLocatorStub.metodos valor="preinvoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Servant preinvoke(byte[] oid, POA adapter, String operation, CookieHolder the_cookie) throws ForwardRequest
~~~

## Parámetros
* **CookieHolder the_cookie**,  {% include w3api/param_description.html metodo=_dato parametro="CookieHolder the_cookie" %}
* **byte[] oid**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] oid" %}
* **String operation**,  {% include w3api/param_description.html metodo=_dato parametro="String operation" %}
* **POA adapter**,  {% include w3api/param_description.html metodo=_dato parametro="POA adapter" %}

## Clase Padre
[_ServantLocatorStub](/Java/_ServantLocatorStub/)

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
