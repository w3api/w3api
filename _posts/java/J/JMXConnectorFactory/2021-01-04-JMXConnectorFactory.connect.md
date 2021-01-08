---
title: JMXConnectorFactory.connect()
permalink: Java/JMXConnectorFactory/connect
date: 2021-01-04
key: JavaJava.J.JMXConnectorFactory
category: java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMXConnectorFactory.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static JMXConnector connect(JMXServiceURL serviceURL) throws IOException
public static JMXConnector connect(JMXServiceURL serviceURL, Map<String,?> environment) throws IOException
~~~

## Parámetros
* **JMXServiceURL serviceURL**,  {% include w3api/param_description.html metodo=_data parametro="JMXServiceURL serviceURL" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_data parametro="?> environment" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[JMXConnectorFactory](/Java/JMXConnectorFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JMXConnectorFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
