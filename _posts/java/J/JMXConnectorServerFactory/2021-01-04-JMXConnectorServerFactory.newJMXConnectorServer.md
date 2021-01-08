---
title: JMXConnectorServerFactory.newJMXConnectorServer()
permalink: Java/JMXConnectorServerFactory/newJMXConnectorServer
date: 2021-01-04
key: JavaJava.J.JMXConnectorServerFactory
category: java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMXConnectorServerFactory.metodos valor="newJMXConnectorServer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static JMXConnectorServer newJMXConnectorServer(JMXServiceURL serviceURL, Map<String,?> environment, MBeanServer mbeanServer) throws IOException
~~~

## Parámetros
* **JMXServiceURL serviceURL**,  {% include w3api/param_description.html metodo=_data parametro="JMXServiceURL serviceURL" %}
* **MBeanServer mbeanServer**,  {% include w3api/param_description.html metodo=_data parametro="MBeanServer mbeanServer" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_data parametro="?> environment" %}

## Excepciones
[JMXProviderException](/Java/JMXProviderException/), [NullPointerException](/Java/NullPointerException/), [MalformedURLException](/Java/MalformedURLException/), [IOException](/Java/IOException/)

## Clase Padre
[JMXConnectorServerFactory](/Java/JMXConnectorServerFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JMXConnectorServerFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
