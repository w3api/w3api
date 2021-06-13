---
title: RMIConnectorServer.toJMXConnector()
permalink: Java/RMIConnectorServer/toJMXConnector
date: 2021-01-11
key: Java.R.RMIConnectorServer
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnectorServer.metodos valor="toJMXConnector" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JMXConnector toJMXConnector(Map<String,?> env) throws IOException
~~~

## Parámetros
* **?&gt; env**,  {% include w3api/param_description.html metodo=_dato parametro="?> env" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalStateException](/Java/IllegalStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[RMIConnectorServer](/Java/RMIConnectorServer/)

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
