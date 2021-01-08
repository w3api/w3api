---
title: ServantLocatorOperations.postinvoke()
permalink: Java/ServantLocatorOperations/postinvoke
date: 2021-01-04
key: JavaJava.S.ServantLocatorOperations
category: java
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
* **String operation**,  {% include w3api/param_description.html metodo=_data parametro="String operation" %}
* **Servant the_servant**,  {% include w3api/param_description.html metodo=_data parametro="Servant the_servant" %}
* **Object the_cookie**,  {% include w3api/param_description.html metodo=_data parametro="Object the_cookie" %}
* **byte[] oid**,  {% include w3api/param_description.html metodo=_data parametro="byte[] oid" %}
* **POA adapter**,  {% include w3api/param_description.html metodo=_data parametro="POA adapter" %}

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
