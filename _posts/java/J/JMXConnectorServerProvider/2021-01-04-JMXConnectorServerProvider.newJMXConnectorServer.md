---
title: JMXConnectorServerProvider.newJMXConnectorServer()
permalink: Java/JMXConnectorServerProvider/newJMXConnectorServer
date: 2021-01-04
key: JavaJava.J.JMXConnectorServerProvider
category: java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMXConnectorServerProvider.metodos valor="newJMXConnectorServer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
JMXConnectorServer newJMXConnectorServer(JMXServiceURL serviceURL, Map<String,?> environment, MBeanServer mbeanServer) throws IOException
~~~

## Parámetros
* **JMXServiceURL serviceURL**,  {% include w3api/param_description.html metodo=_data parametro="JMXServiceURL serviceURL" %}
* **MBeanServer mbeanServer**,  {% include w3api/param_description.html metodo=_data parametro="MBeanServer mbeanServer" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_data parametro="?> environment" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[JMXConnectorServerProvider](/Java/JMXConnectorServerProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JMXConnectorServerProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
