---
title: RMIConnector.RMIConnector()
permalink: Java/RMIConnector/RMIConnector
date: 2021-01-11
key: Java.R.RMIConnector
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnector.constructores valor="RMIConnector" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RMIConnector(JMXServiceURL url, Map<String,?> environment)
public RMIConnector(RMIServer rmiServer, Map<String,?> environment)
~~~

## Parámetros
* **JMXServiceURL url**,  {% include w3api/param_description.html metodo=_dato parametro="JMXServiceURL url" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}
* **RMIServer rmiServer**,  {% include w3api/param_description.html metodo=_dato parametro="RMIServer rmiServer" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RMIConnector](/Java/RMIConnector/)

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
