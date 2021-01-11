---
title: JMXConnectorProvider.newJMXConnector()
permalink: Java/JMXConnectorProvider/newJMXConnector
date: 2021-01-11
key: JavaJava.J.JMXConnectorProvider
category: java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMXConnectorProvider.metodos valor="newJMXConnector" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
JMXConnector newJMXConnector(JMXServiceURL serviceURL, Map<String,?> environment) throws IOException
~~~

## Parámetros
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}
* **JMXServiceURL serviceURL**,  {% include w3api/param_description.html metodo=_dato parametro="JMXServiceURL serviceURL" %}

## Excepciones
[IOException](/Java/IOException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[JMXConnectorProvider](/Java/JMXConnectorProvider/)

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
