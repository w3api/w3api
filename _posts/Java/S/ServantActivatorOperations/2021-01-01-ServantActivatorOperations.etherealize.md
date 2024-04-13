---
title: ServantActivatorOperations.etherealize()
permalink: /Java/ServantActivatorOperations/etherealize/
date: 2021-01-11
key: Java.S.ServantActivatorOperations
category: Java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServantActivatorOperations.metodos valor="etherealize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void etherealize(byte[] oid, POA adapter, Servant serv, boolean cleanup_in_progress, boolean remaining_activations)
~~~

## Parámetros
* **boolean cleanup_in_progress**,  {% include w3api/param_description.html metodo=_dato parametro="boolean cleanup_in_progress" %}
* **byte[] oid**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] oid" %}
* **boolean remaining_activations**,  {% include w3api/param_description.html metodo=_dato parametro="boolean remaining_activations" %}
* **POA adapter**,  {% include w3api/param_description.html metodo=_dato parametro="POA adapter" %}
* **Servant serv**,  {% include w3api/param_description.html metodo=_dato parametro="Servant serv" %}

## Clase Padre
[ServantActivatorOperations](/Java/ServantActivatorOperations/)

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
