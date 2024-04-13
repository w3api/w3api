---
title: ServantLocatorOperations.postinvoke()
permalink: /Java/ServantLocatorOperations/postinvoke/
date: 2021-01-11
key: Java.S.ServantLocatorOperations
category: Java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServantLocatorOperations.metodos valor="postinvoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void postinvoke(byte[] oid, POA adapter, String operation, Object the_cookie, Servant the_servant)
~~~

## Parámetros
* **byte[] oid**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] oid" %}
* **String operation**,  {% include w3api/param_description.html metodo=_dato parametro="String operation" %}
* **Object the_cookie**,  {% include w3api/param_description.html metodo=_dato parametro="Object the_cookie" %}
* **POA adapter**,  {% include w3api/param_description.html metodo=_dato parametro="POA adapter" %}
* **Servant the_servant**,  {% include w3api/param_description.html metodo=_dato parametro="Servant the_servant" %}

## Clase Padre
[ServantLocatorOperations](/Java/ServantLocatorOperations/)

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
