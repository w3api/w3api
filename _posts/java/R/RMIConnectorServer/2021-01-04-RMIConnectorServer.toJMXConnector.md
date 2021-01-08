---
title: RMIConnectorServer.toJMXConnector()
permalink: Java/RMIConnectorServer/toJMXConnector
date: 2021-01-04
key: JavaJava.R.RMIConnectorServer
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
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **?&gt; env**,  {% include w3api/param_description.html metodo=_data parametro="?> env" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

## Clase Padre
[RMIConnectorServer](/Java/RMIConnectorServer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RMIConnectorServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
