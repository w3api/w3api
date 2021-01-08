---
title: ServantActivatorOperations.etherealize()
permalink: Java/ServantActivatorOperations/etherealize
date: 2021-01-04
key: JavaJava.S.ServantActivatorOperations
category: java
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
* **Servant serv**,  {% include w3api/param_description.html metodo=_data parametro="Servant serv" %}
* **byte[] oid**,  {% include w3api/param_description.html metodo=_data parametro="byte[] oid" %}
* **boolean cleanup_in_progress**,  {% include w3api/param_description.html metodo=_data parametro="boolean cleanup_in_progress" %}
* **boolean remaining_activations**,  {% include w3api/param_description.html metodo=_data parametro="boolean remaining_activations" %}
* **POA adapter**,  {% include w3api/param_description.html metodo=_data parametro="POA adapter" %}

## Clase Padre
[ServantActivatorOperations](/Java/ServantActivatorOperations/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServantActivatorOperations.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
