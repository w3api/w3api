---
title: _ServantLocatorStub.postinvoke()
permalink: Java/_ServantLocatorStub/postinvoke
date: 2021-01-11
key: JavaJava._._ServantLocatorStub
category: java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java._._ServantLocatorStub.metodos valor="postinvoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void postinvoke(byte[] oid, POA adapter, String operation, Object the_cookie, Servant the_servant)
~~~

## Parámetros
* **byte[] oid**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] oid" %}
* **String operation**,  {% include w3api/param_description.html metodo=_dato parametro="String operation" %}
* **Object the_cookie**,  {% include w3api/param_description.html metodo=_dato parametro="Object the_cookie" %}
* **POA adapter**,  {% include w3api/param_description.html metodo=_dato parametro="POA adapter" %}
* **Servant the_servant**,  {% include w3api/param_description.html metodo=_dato parametro="Servant the_servant" %}

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
